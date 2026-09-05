import React, { useEffect, useState } from 'react';
import { Navbar } from './components/layout/Navbar';
import { Sidebar, NavigationTab } from './components/layout/Sidebar';
import { CommandCenter } from './pages/CommandCenter';
import { RecoveryQueue } from './pages/RecoveryQueue';
import { CaseDetail } from './pages/CaseDetail';
import { DecisionExplorer } from './pages/DecisionExplorer';
import { Experiments } from './pages/Experiments';
import { SimulatorPage } from './pages/SimulatorPage';
import { GovernanceSafety } from './pages/GovernanceSafety';
import { DemoShowcase } from './pages/DemoShowcase';
import { api } from './services/api';
import { AnalyticsOverview, Case } from './types';

export function App() {
  const [activeTab, setActiveTab] = useState<NavigationTab>('command-center');
  const [selectedCaseId, setSelectedCaseId] = useState<string | null>(null);
  const [analytics, setAnalytics] = useState<AnalyticsOverview | null>(null);
  const [cases, setCases] = useState<Case[]>([]);
  const [isRefreshing, setIsRefreshing] = useState(false);

  const fetchGlobalData = async () => {
    setIsRefreshing(true);
    try {
      const [overview, caseList] = await Promise.all([
        api.getAnalytics().catch(() => null),
        api.getCases().catch(() => []),
      ]);
      setAnalytics(overview);
      setCases(caseList);
    } catch (err) {
      console.error('Error loading global data:', err);
    } finally {
      setIsRefreshing(false);
    }
  };

  useEffect(() => {
    fetchGlobalData();
  }, []);

  const handleSelectCase = (caseId: string) => {
    setSelectedCaseId(caseId);
  };

  const handleBackToQueue = () => {
    setSelectedCaseId(null);
  };

  const handleGenerateBatch = async () => {
    try {
      await api.generateBatch(25);
      await fetchGlobalData();
    } catch (err) {
      console.error(err);
    }
  };

  const suppressedCount = analytics?.kpis.cases_suppressed_by_safety || 0;

  return (
    <div className="min-h-screen bg-[#0B0F19] text-slate-100 flex flex-col">
      {/* Top Navbar */}
      <Navbar
        onRefresh={fetchGlobalData}
        onOpenDemo={() => {
          setSelectedCaseId(null);
          setActiveTab('demo');
        }}
        onGenerateBatch={handleGenerateBatch}
        isRefreshing={isRefreshing}
      />

      <div className="flex-1 flex">
        {/* Left Sidebar */}
        <Sidebar
          activeTab={activeTab}
          onTabChange={(tab) => {
            setSelectedCaseId(null);
            setActiveTab(tab);
          }}
          casesCount={cases.length}
          suppressedCount={suppressedCount}
        />

        {/* Main Content View */}
        <main className="flex-1 p-6 md:p-8 max-w-7xl mx-auto w-full overflow-y-auto">
          {selectedCaseId ? (
            <CaseDetail
              caseId={selectedCaseId}
              onBack={handleBackToQueue}
              onRefreshList={fetchGlobalData}
            />
          ) : (
            <>
              {activeTab === 'command-center' && (
                <CommandCenter
                  analytics={analytics}
                  cases={cases}
                  onSelectCase={handleSelectCase}
                  onNavigateTab={(tab) => setActiveTab(tab)}
                />
              )}

              {activeTab === 'recovery-queue' && (
                <RecoveryQueue
                  cases={cases}
                  onSelectCase={handleSelectCase}
                  onEvaluateCase={async (id) => {
                    await api.evaluateDecision(id);
                    await fetchGlobalData();
                  }}
                />
              )}

              {activeTab === 'decision-explorer' && <DecisionExplorer />}

              {activeTab === 'experiments' && <Experiments />}

              {activeTab === 'simulator' && (
                <SimulatorPage
                  onSelectCase={handleSelectCase}
                  onRefreshList={fetchGlobalData}
                />
              )}

              {activeTab === 'governance' && <GovernanceSafety />}

              {activeTab === 'demo' && (
                <DemoShowcase
                  onSelectCase={handleSelectCase}
                  onRefreshList={fetchGlobalData}
                />
              )}
            </>
          )}
        </main>
      </div>
    </div>
  );
}

export default App;
